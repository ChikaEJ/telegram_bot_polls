import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from user.models import PollModel, UserProfileModel

from .telegram import send_message, send_poll


@csrf_exempt
def telegram_webhook(request):
    data = json.loads(request.body)

    if "message" in data and "text" in data["message"]:
        chat_id = data["message"]["chat"]["id"]
        text = data["message"]["text"]

        if text == "/start":
            user, created = UserProfileModel.objects.get_or_create(
                telegram_chat_id=chat_id
            )
            send_message(chat_id, "Вы зарегистрированны!\n/poll")

        elif text == "/poll":
            try:
                poll = PollModel.objects.latest("created_at")
                send_poll(chat_id, poll)
            except PollModel.DoesNotExist:
                send_message(chat_id, "Опросников нет!")

    elif "poll_answer" in data:
        print(data["poll_answer"])
        answer = data["poll_answer"]
        poll_id = answer["poll_id"]
        user_chat_id = answer["user"]["id"]
        selected = answer["option_ids"]

        try:
            user = UserProfileModel.objects.get(telegram_chat_id=user_chat_id)
            poll = PollModel.objects.get(poll_id=poll_id)
            user.completed_polls += 1
            user.save()
            poll.user_options.append(selected)
            poll.save()
        except Exception as e:
            print(e)
    return HttpResponse({"ok", True})
