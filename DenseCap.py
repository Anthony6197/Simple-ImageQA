
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

def DenseCaptioning(imgPath):
    key = "e269851e05694b46b94fbd6b6dfdc48b"
    endpoint = "https://jarvis-h.cognitiveservices.azure.com/"
    creds = CognitiveServicesCredentials(key)
    client = ComputerVisionClient(endpoint, creds)
    with open(imgPath, 'rb') as img:
        result = client.analyze_image_in_stream(img, [VisualFeatureTypes.adult,
                                                            VisualFeatureTypes.brands,
                                                            VisualFeatureTypes.categories,
                                                            VisualFeatureTypes.color,
                                                            VisualFeatureTypes.description,
                                                            VisualFeatureTypes.faces,
                                                            VisualFeatureTypes.image_type,
                                                            VisualFeatureTypes.objects,
                                                            VisualFeatureTypes.tags])
    
    tags = result.tags
    brands = result.brands
    categories = result.categories
    color = result.color
    description = result.description
    faces = result.faces
    image_type = result.image_type
    objects = result.objects
    readable_res = "Image Tags:\n"
    for tag in tags:
        readable_res += f"- {tag.name} (confidence: {tag.confidence})\n"

    if len(brands) > 0:
        readable_res += "\nBrands:\n"
        for brand in brands:
            readable_res += f"- {brand.name} (confidence: {brand.confidence})\n"
    
    readable_res += "\nCategories:\n"
    for category in categories:
        readable_res += f"- {category.name} (confidence: {category.score})\n"

    readable_res += "\nDominant Color:\n"
    readable_res += f"- Background Color: {color.dominant_color_background}\n"
    readable_res += f"- Foreground Color: {color.dominant_color_foreground}\n"
    readable_res += f"- Accent Color: {color.accent_color}\n"
    
    if len(description.captions) > 0:
        readable_res += "\nImage Description:\n"
        for caption in description.captions:
            readable_res += f"- {caption.text} (confidence: {caption.confidence})\n"
    
    if len(faces) > 0:
        readable_res += "\nFaces:\n"
        for face in faces:
            readable_res += f"- Gender: {face.gender}\n"
            readable_res += f"- Age: {face.age}\n"
            # readable_res += f"- Emotion: {face.emotion}\n"
    
    if image_type.clip_art_type != 0:
        readable_res += "- Clip Art Detected\n"
    elif image_type.line_drawing_type != 0:
        readable_res += "- Line Drawing Detected\n"
    
    if len(objects) > 0:
        readable_res += "\nObjects:\n"
        for obj in objects:
            readable_res += f"- {obj.object_property} (confidence: {obj.confidence})\n"
    
    return(readable_res)