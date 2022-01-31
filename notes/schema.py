import graphene
from graphene_django import DjangoObjectType
from .models import Note
from django.db import models


class NoteType(DjangoObjectType):
    class Meta:
        model = Note
        fields = (
            'id',
            'title',
            'pub_date',
            'description',
        )


class Query(graphene.ObjectType):
    notes = graphene.List(NoteType)

    def resolve_notes(self, info):
        return Note.objects.all()


class NoteInput(graphene.InputObjectType):
    title = graphene.String()
    pub_date = graphene.Date()
    description = graphene.String()


class NoteEditInput(graphene.InputObjectType):
    title = graphene.String()
    description = graphene.String()


class CreateNote(graphene.Mutation):
    class Arguments:
        input = NoteInput(required=True)

    note = graphene.Field(NoteType)

    @classmethod
    def mutate(cls, root, info, input):
        note = Note()
        note.title = input.title
        note.pub_date = input.pub_date
        note.description = input.description
        note.save()
        return CreateNote(note=note)


class UpdateNote(graphene.Mutation):
    class Arguments:
        input = NoteEditInput(required=True)
        id = graphene.ID()

    note = graphene.Field(NoteType)
    @classmethod
    def mutate(cls, root, info, input, id):
        note = Note.objects.get(pk=id)
        note.title = input.title
        note.description = input.description
        note.save()

        return UpdateNote(note=note)


class DeleteNote(graphene.Mutation):
    ok = graphene.Boolean()

    class Arguments:
        id = graphene.ID()

    @classmethod
    def mutate(cls, root, info, **kwargs):
        note = Note.objects.get(pk=kwargs["id"])
        note.delete()
        return cls(ok=True)


class Mutation(graphene.ObjectType):
    update_note = UpdateNote.Field()
    create_note = CreateNote.Field()
    delete_note = DeleteNote.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
