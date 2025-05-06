from django.contrib.sites import requests
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

FASTAPI_URL = "https://93c7-35-240-154-247.ngrok-free.app/generate"

@csrf_exempt
@api_view(['POST'])
def chat_generate(request):
    """Send request to FastAPI and return response"""
    prompt = request.data.get("prompt")

    if not prompt:
        return Response({"error": "Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        response = requests.post(FASTAPI_URL, json={"prompt": prompt}, timeout=500)
        response.raise_for_status()  # Raise error if request failed

        # Check if FastAPI returns a non-200 status
        if response.status_code != 200:
            return Response({"error": "FastAPI returned an error", "details": response.json()},
                            status=response.status_code)

        return Response(response.json(), status=response.status_code)

    except requests.exceptions.RequestException as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)