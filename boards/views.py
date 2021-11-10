from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Board, Comment
from .serializers import BoardSerializers, BoardDetailSerializers, CommentSerializers



class ListBoardsView(APIView):
    def get(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializers(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        boards = Board.objects.all()
        serializer = BoardSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DetailBoardView(APIView):
    def get(self, request, pk):
        if not Board.objects.filter(id=pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        board = Board.objects.get(id=pk)
        serialize = BoardDetailSerializers(board)
        return Response(serialize.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        if not Board.objects.filter(id=pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        board = Board.objects.get(id=pk)
        serializer = BoardSerializers(board, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        if not Board.objects.filter(id=pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        board = Board.objects.get(id=pk)
        board.delete()
        return Response(status=status.HTTP_200_OK)


class CommentsView(APIView):
    def post(self, request, pk):
        if not Board.objects.filter(id=pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        board = Board.objects.get(id=pk)
        request.data['board'] = board.id
        serializer = CommentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateCommentsView(APIView):
    def delete(self, request, pk, comment_pk):
        if not Comment.objects.filter(id=comment_pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        comment = Comment.objects.get(id=comment_pk)
        comment.delete()
        return Response(status=status.HTTP_200_OK)

    def put(self, request, pk, comment_pk):
        if not Comment.objects.filter(id=comment_pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        comment = Comment.objects.get(pk=comment_pk)
        serializer = CommentSerializers(comment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_200_OK)
        return Response(status = status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk, comment_pk):
        if not Comment.objects.filter(id=comment_pk).exists():
            return Response(status = status.HTTP_404_NOT_FOUND)
        comment = Comment.objects.get(id=comment_pk)
        serialize = CommentSerializers(comment)
        return Response(serialize.data, status=status.HTTP_200_OK)