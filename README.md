# translation_unicode_converter
 
Converts the translation file of a custom component to Unicode.

# usage

```
sensor:
  - platform: translation_unicode_converter
    components:
      - name: weight_recorder
        sort: false  # If true, sorts the contents of the json file
```