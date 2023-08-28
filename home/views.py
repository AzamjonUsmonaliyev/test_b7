from django.shortcuts import render
from django.http import HttpResponse

def helloview(request):
    return HttpResponse("""
    
    <!DOCTYPE html>
<html lang="en">
<head>
<title>CSS Template</title>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
* {
  box-sizing: border-box;
}

</html>

""")
