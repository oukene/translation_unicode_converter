# translation_unicode_converter
 
Converts the translation file of a custom component to Unicode.

# usage

```
sensor:
  - platform: translation_unicode_converter
    components:
      - name: custom_component_name # Enter the folder name of the custom component.
        sort: false  # If true, sorts the contents of the json file
```