# Icon Assets

## Required Icon: icon.png

The main application icon (`icon.png`) should be placed in this directory or in the root of the repository.

### Requirements:
- Format: PNG
- Recommended size: 512x512 pixels or larger
- Transparent background preferred
- Should represent the Echo-Crystal AGI system branding

### Usage:
- Desktop launchers (`.desktop` files)
- Application packaging (Windows, macOS, Linux)
- Mobile apps (iOS, Android)
- Web interface favicon (after conversion)

### Current Status:
The icon file needs to be provided from the echovoice project at:
`/home/jacob/Desktop/echovoice/icon.png`

Copy this file to:
- `icons/icon.png` (recommended), or
- `icon.png` (root directory)

### Platform-Specific Icons:

Different platforms may require different icon formats:
- **Windows**: .ico (multiple sizes)
- **macOS**: .icns
- **Linux**: .png (various sizes)
- **Android**: .png (various densities)
- **iOS**: .png (various sizes for different devices)

Use the setup_icon.sh script to generate platform-specific icons from the source icon.png file.
