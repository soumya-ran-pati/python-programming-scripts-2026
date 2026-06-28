url = input("Enter the url of the video: ")
watch_id = url.split("=", 1)[1]
generated_url = f"""https://www.yout-ube.com/watch?v={watch_id}"""
print("Paste this url: " + generated_url)
