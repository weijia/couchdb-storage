from rest_framework import serializers
from rest_framework import generics
from rest_framework import permissions


def get_serializer(class_inst):
    meta_class = type("Meta", tuple(), {"model": class_inst})
    return type(class_inst.__name__ + "Serializer", tuple([serializers.ModelSerializer]),
                {"Meta": meta_class}
                )


def get_api_class(class_inst, suffix="List", parent=[generics.ListCreateAPIView]):
    serializer = get_serializer(class_inst)
    return type(class_inst.__name__ + suffix, tuple(parent),
                {
                    "queryset": class_inst.objects.all(),
                    "serializer_class": serializer,
                    'permission_classes': (permissions.IsAuthenticatedOrReadOnly,)
                }
                )


def get_create_api_class(class_inst):
    return get_api_class(class_inst)


def get_detail_api_class(class_inst):
    return get_api_class(class_inst, "Detail", [generics.RetrieveUpdateDestroyAPIView])
