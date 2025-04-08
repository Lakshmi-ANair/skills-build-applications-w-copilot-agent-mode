from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Team, Activity, Leaderboard, Workout
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class ActivityViewSet(ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer

class LeaderboardViewSet(ModelViewSet):
    queryset = Leaderboard.objects.all()
    serializer_class = LeaderboardSerializer

class WorkoutViewSet(ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': 'https://cuddly-yodel-jj99qjqvw6jwc95g-8000.app.github.dev/api/users/',
        'teams': 'https://cuddly-yodel-jj99qjqvw6jwc95g-8000.app.github.dev/api/teams/',
        'activities': 'https://cuddly-yodel-jj99qjqvw6jwc95g-8000.app.github.dev/api/activities/',
        'leaderboard': 'https://cuddly-yodel-jj99qjqvw6jwc95g-8000.app.github.dev/api/leaderboard/',
        'workouts': 'https://cuddly-yodel-jj99qjqvw6jwc95g-8000.app.github.dev/api/workouts/',
    })
