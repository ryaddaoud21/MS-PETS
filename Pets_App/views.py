import json

import requests
from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from .models import *
from rest_framework import serializers, status


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

from rest_framework import serializers
class FoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Found
        fields = '__all__'

class LostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lost
        fields = '__all__'


def homepage(request):
    return HttpResponse('hello')





def postlist(request):
    data = list(Post.objects.values())
    print(data)
    return JsonResponse(data, safe=False)


def lostlist(request):
    data = list(Lost.objects.values())
    print(data)
    return JsonResponse(data, safe=False)

def foundlist(request):
    data = list(Found.objects.values())
    print(data)
    return JsonResponse(data, safe=False)


def Commentlist(request):
    data = list(Comment.objects.values())
    print(data)
    return JsonResponse(data, safe=False)

def detailpost(post_id):
    commentlist = Comment.objects.filter(post=post_id).values()
    data = list(commentlist)
    print(data)
    return JsonResponse(data, safe=False)





def addlost(request):
    print(request.META['HTTP_AUTHORIZATION'])
    url = 'http://localhost:8090/api/verify?token=' + request.META['HTTP_AUTHORIZATION']
    myobj = {'somekey': 'somevalue'}

    # use the 'headers' parameter to set the HTTP headers:
    x = requests.get(url, data=myobj, headers={"HTTP_HOST": "MyVeryOwnHost"})
    response = json.loads(x.text)
    print(response["message"])

    if (response["message"] == "Unvalid"):
        data = [{'message': response["message"]}]
        return JsonResponse(data, safe=False)
    else:
        userid = response["userid"]  # fromspring
        body = json.loads(request.body)
        body["by"] = userid
        img_str = body["Image"]
        body.pop('Image', None)
        u = Lost(**body)
        u.Image = decode_base64_file(img_str)
        u.save()
        data = LostSerializer(instance=u).data

        return JsonResponse(data,safe=False,status=status.HTTP_500_INTERNAL_SERVER_ERROR)



def addfound(request):
        print(request.META['HTTP_AUTHORIZATION'])
        url = 'http://localhost:8090/api/verify?token=' + request.META['HTTP_AUTHORIZATION']
        myobj = {'somekey': 'somevalue'}

        # use the 'headers' parameter to set the HTTP headers:
        x = requests.get(url, data=myobj, headers={"HTTP_HOST": "MyVeryOwnHost"})
        response = json.loads(x.text)
        print(response["message"])

        if (response["message"] == "Unvalid"):
            data = [{'message': response["message"]}]
            return JsonResponse(data, safe=False)
        else:
            userid = response["userid"]  # fromspring
            body = json.loads(request.body)
            body["by"] = userid
            img_str = body["Image"]
            body.pop('Image', None)
            u = Found(**body)
            u.Image = decode_base64_file(img_str)
            u.save()
            data = FoundSerializer(instance=u).data

            return JsonResponse(data, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def decode_base64_file(data):

    def get_file_extension(file_name, decoded_file):
        import imghdr

        extension = imghdr.what(file_name, decoded_file)
        extension = "jpg" if extension == "jpeg" else extension

        return extension

    from django.core.files.base import ContentFile
    import base64
    import six
    import uuid

    # Check if this is a base64 string
    if isinstance(data, six.string_types):
        # Check if the base64 string is in the "data:" format
        if 'data:' in data and ';base64,' in data:
            # Break out the header from the base64 content
            header, data = data.split(';base64,')

        # Try to decode the file. Return validation error if it fails.
        try:
            decoded_file = base64.b64decode(data)
        except TypeError:
            TypeError('invalid_image')

        # Generate file name:
        file_name = str(uuid.uuid4())[:12] # 12 characters are more than enough.
        # Get the file name extension:
        file_extension = get_file_extension(file_name, decoded_file)

        complete_file_name = "%s.%s" % (file_name, file_extension, )

        return ContentFile(decoded_file, name=complete_file_name)




def addpost(request):


    print(request.META['HTTP_AUTHORIZATION'])
    url = 'http://localhost:8090/api/verify?token=' + request.META['HTTP_AUTHORIZATION']
    myobj = {'somekey': 'somevalue'}

    # use the 'headers' parameter to set the HTTP headers:
    x = requests.get(url, data=myobj, headers={"HTTP_HOST": "MyVeryOwnHost"})
    response = json.loads(x.text)
    print(response["message"])

    if (response["message"] == "Unvalid"):
        data = [{'message': response["message"]}]
        return JsonResponse(data, safe=False)
    else:
        userid = response["userid"] #fromspring
        body = json.loads(request.body)
        body["by"] = userid
        img_str = body["image"]
        body.pop('image', None)
        u = Post(**body)
        u.image = decode_base64_file(img_str)
        u.save()
        data = PostSerializer(instance=u).data
        return JsonResponse(data, safe=False)




def foundbyuser(request):
    print(request.META['HTTP_AUTHORIZATION'])
    url = 'http://localhost:8090/api/verify?token=' + request.META['HTTP_AUTHORIZATION']
    myobj = {'somekey': 'somevalue'}

    # use the 'headers' parameter to set the HTTP headers:
    x = requests.get(url, data=myobj, headers={"HTTP_HOST": "MyVeryOwnHost"})
    response = json.loads(x.text)
    print(response["message"])

    if (response["message"] == "Unvalid"):
        data = [{'message': response["message"]}]
        return JsonResponse(data, safe=False)
    else:
        userid = response["userid"]  # fromspring
        founds = Found.objects.filter(by=userid).values()
        data = list(founds)
        return JsonResponse(data, safe=False)


def lostbyuser(request):

        print(request.META['HTTP_AUTHORIZATION'])
        url = 'http://localhost:8090/api/verify?token=' + request.META['HTTP_AUTHORIZATION']
        myobj = {'somekey': 'somevalue'}

        # use the 'headers' parameter to set the HTTP headers:
        x = requests.get(url, data=myobj, headers={"HTTP_HOST": "MyVeryOwnHost"})
        response = json.loads(x.text)
        print(response["message"])

        if (response["message"] == "Unvalid"):
            data = [{'message': response["message"]}]
            return JsonResponse(data, safe=False)
        else:
            userid = response["userid"]  # fromspring
            losts = Lost.objects.filter(by=userid).values()
            data = list(losts)
            return JsonResponse(data, safe=False)


def addcomment(request):


    print(request.META['HTTP_AUTHORIZATION'])
    url = 'http://localhost:8090/api/verify?token=' + request.META['HTTP_AUTHORIZATION']
    myobj = {'somekey': 'somevalue'}

    # use the 'headers' parameter to set the HTTP headers:
    x = requests.get(url, data=myobj, headers={"HTTP_HOST": "MyVeryOwnHost"})
    response = json.loads(x.text)
    print(response["message"])

    if (response["message"] == "Unvalid"):
        data = [{'message': response["message"]}]
        return JsonResponse(data, safe=False)
    else:
        userid = response["userid"] #fromspring
        body = json.loads(request.body)
        body["by"] = userid
        u = Comment(**body)
        u.save()
        data = CommentSerializer(instance=u).data
        return JsonResponse(data, safe=False)

