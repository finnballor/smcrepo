from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Course, Subject , Teacher
from .serializers import CourseSerializer , SubjectSerializer, TeacherSerializer
# Create your views here.


@api_view(['GET'])
def courseList(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addCourse(request):
    serializer = CourseSerializer( data=request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateCourse(request, pk):
    course = Course.objects.get(id=pk)
    serializer = CourseSerializer(instance=course, data=request.data, many= False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def deleteCourse(request,pk):
    course  = Course.objects.get(id=pk)
    course.delete()
    return Response('Course Deleted Successfully.')





@api_view(['GET'])
def teacherList(request):
    teachers = Teacher.objects.all()
    serializer = TeacherSerializer(teachers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addTeacher(request):
    serializer = TeacherSerializer( data=request.data )
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def updateTeacher(request, pk):
    teacher = Teacher.objects.get(id=pk)
    serializer = TeacherSerializer(instance=teacher, data=request.data, many= False)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def deleteTeacher(request,pk):
    teacher  = Teacher.objects.get(id=pk)
    teacher.delete()
    return Response('Teacher Record Deleted Successfully.')




