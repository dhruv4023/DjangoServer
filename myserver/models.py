from datetime import datetime
# project data
class Project:
    def __init__(self, title, link, description):
        self.title = title
        self.link = link
        self.description = description
        self.postedOn = datetime.now()


class ChatData:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.chat_mess_on = datetime.now()
        self.messages = []

    def __str__(self):
        return self.name


class MessageList:
    def __init__(self, side, message):
        self.side = side
        self.message = message
        self.messaged_on = datetime.now()


# contactForm data
class ContactFormData:
    def __init__(self, name, email, msg):
        self.name = name
        self.email = email
        self.msg = msg
        self.messagedOn = datetime.now()

    def __str__(self):
        return self.name

# from django.db import models

# # project data
# class Project(models.Model):
#     title = models.CharField(max_length=255)
#     link = models.CharField(max_length=255)
#     description = models.CharField(max_length=255)
#     postedOn = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.title

# # chat data
# class ChatData(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     chat_mess_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

# class MessageList(models.Model):
#     chat_data = models.ForeignKey(ChatData, on_delete=models.CASCADE)
#     side = models.CharField(max_length=255)
#     message = models.TextField()
#     messaged_on = models.DateTimeField(auto_now_add=True)


# # contactForm data
# class ContactFormData(models.Model):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255)
#     message = models.CharField(max_length=255)
#     messagedOn = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name
