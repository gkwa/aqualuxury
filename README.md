# aqualuxury


Aqualuxury is a Python tool designed to extract image URLs from Instagram posts.

## Description

Aqualuxury takes one or more Instagram post URLs as input and extracts the associated image URLs. It's useful for quickly obtaining direct links to images from Instagram posts without manually inspecting the page source.

## Usage

To use Aqualuxury, run the following command:

```
python -m aqualuxury <url1> <url2> ...
```

Replace `<url1>`, `<url2>`, etc. with the Instagram post URLs you want to process.

Example:

```
python -m aqualuxury https://www.instagram.com/p/ABC123/ https://www.instagram.com/p/XYZ789/
```

This will output the original URLs along with their corresponding image URLs:

```
Original URL: https://www.instagram.com/p/ABC123/
Image URL: https://scontent-example.cdninstagram.com/image1.jpg

Original URL: https://www.instagram.com/p/XYZ789/
Image URL: https://scontent-example.cdninstagram.com/image2.jpg
```

Note: Duplicate URLs in the input will be automatically removed to avoid redundant processing.