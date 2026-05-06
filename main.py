from pyscript import document, display

def display_message():
    message = """School Yearbook
    
    Various photos taken from SY 2025-2026, including photos of students, teachers, and school events. The yearbook captures the memories and highlights of the school year, showcasing the diversity and spirit of the school community. It serves as a keepsake for students and staff to look back on their experiences and celebrate their achievements throughout the year.
    """

    output_element = document.getElementById("description")
    output_element.innerText = message