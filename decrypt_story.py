import caesar_cipher as cc

file_path = "story.txt" 
story = cc.get_story_string(file_path)
 
def decrypt_story(story):   
    return cc.CiphertextMessage(story).decrypt_message()

print(decrypt_story(story))
