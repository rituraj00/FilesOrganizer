import os
import shutil

extensions = {
    "images": {
        '.jpg': 'JPEG image',
        '.jpeg': 'JPEG image',
        '.png': 'Portable Network Graphics image',
        '.gif': 'Graphical Interchange Format image',
        '.bmp': 'Bitmap image',
        '.tiff': 'Tagged Image File Format',
        '.tif': 'Tagged Image File Format',
        '.webp': 'WebP image',
        '.svg': 'Scalable Vector Graphics image',
        '.psd': 'Adobe Photoshop Document',
        '.ai': 'Adobe Illustrator Document',
        '.eps': 'Encapsulated PostScript',
        '.raw': 'Camera raw image',
        '.cr2': 'Canon Raw Image File',
        '.nef': 'Nikon Electronic Format Image',
        '.orf': 'Olympus Raw Format Image',
        '.sr2': 'Sony Raw Format Image',
    },
    "videos": {
        ".mp4": "MPEG-4 video file",
        ".avi": "Audio Video Interleave movie or sound file",
        ".mov": "Apple QuickTime movie file",
        ".wmv": "Windows Media Video file",
        ".mkv": "Matroska Video file",
        ".flv": "Flash-compatible video file",
        ".webm": "WebM video file",
        ".vob": "Video object file",
        ".mpg": "MPEG 1 system stream",
        ".mpeg": "Moving Picture Experts Group movie file",
        ".m4v": "MPEG-4 video file",
        ".3gp": "3GPP multimedia file",
        ".3g2": "3GPP2 multimedia file",
        ".rm": "RealMedia file",
        ".swf": "Shockwave Flash file",
        ".asf": "Advanced Systems Format file",
        ".divx": "DivX-encoded movie file",
        ".m2ts": "Blu-ray BDAV Video file",
        ".mpe": "MPEG movie file",
        ".ogv": "Ogg Video file"
    },
    "documents": {
        '.doc': 'Microsoft Word document (pre-2007)',
        '.docx': 'Microsoft Word document',
        '.pdf': 'Portable Document Format file',
        '.rtf': 'Rich Text Format file',
        '.odt': 'OpenDocument Text document',
        '.txt': 'Unformatted text file',
        '.ppt': 'Microsoft PowerPoint presentation (pre-2007)',
        '.pptx': 'Microsoft PowerPoint presentation',
        '.xls': 'Microsoft Excel spreadsheet (pre-2007)',
        '.xlsx': 'Microsoft Excel spreadsheet',
        '.csv': 'Comma-separated values file',
        '.odp': 'OpenDocument Presentation',
        '.ods': 'OpenDocument Spreadsheet',
        '.pps': 'Microsoft PowerPoint slideshow (pre-2007)',
        '.ppsx': 'Microsoft PowerPoint slideshow',
        '.odg': 'OpenDocument Drawing',
        '.odf': 'OpenDocument Formula',
        '.odm': 'OpenDocument Master document',
        '.docm': 'Microsoft Word macro-enabled document',
        '.dotx': 'Microsoft Word template'
    },
    "programs": {
        ".py": "Python",
        ".java": "Java",
        ".js": "JavaScript",
        ".c": "C",
        ".cpp": "C++",
        ".cs": "C#",
        ".php": "PHP",
        ".html": "HTML",
        ".css": "CSS",
        ".rb": "Ruby",
        ".go": "Go",
        ".swift": "Swift",
        ".kt": "Kotlin",
        ".pl": "Perl",
        ".lua": "Lua",
        ".ts": "TypeScript",
        ".scala": "Scala",
        ".dart": "Dart",
        ".rs": "Rust",
        ".sh": "Bash",
        ".exe": "Executable",
        ".msi": "Microsoft Installer",
    }
}

dirs_to_create = {
    "images": [],
    "videos": [],
    "documents": [],
    "programs": []
}

current_path = os.getcwd()

current_directory_files = os.listdir()

for file in os.listdir():
    filename, extension = os.path.splitext(file)
    if extension != '':
        if extensions["images"].__contains__(extension):
            dirs_to_create["images"].append(file)
        elif extensions["documents"].__contains__(extension):
            dirs_to_create["documents"].append(file)
        elif extensions["videos"].__contains__(extension):
            dirs_to_create["videos"].append(file)
        elif extensions["programs"].__contains__(extension):
            dirs_to_create["programs"].append(file)
        else:
            continue

for category in dirs_to_create.keys():
    if len(dirs_to_create[category]) > 0:
        if not os.path.exists(f'{os.getcwd()}\\{category.title()}'):
            os.mkdir(f'{os.getcwd()}\\{category.title()}')
        for file in dirs_to_create[category]:
            dest_path = f'{os.getcwd()}\\{category.title()}\\{file}'
            src_path = f'{os.getcwd()}\\{file}'
            shutil.move(src_path, dest_path)

print("Success")





