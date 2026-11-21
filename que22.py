import os
import xml.etree.ElementTree as ET


def create_sample_xml(filename="library_catalog.xml"):
    sample_xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<library name="Central City Library" city="Bengaluru">
    <book id="BK101" category="Programming">
        <title>Clean Code</title>
        <author>Robert C. Martin</author>
        <year>2008</year>
        <price currency="INR">650.00</price>
    </book>
    <book id="BK102" category="Data Science">
        <title>Python for Data Analysis</title>
        <author>Wes McKinney</author>
        <year>2022</year>
        <price currency="INR">890.00</price>
    </book>
    <book id="BK103" category="Algorithms">
        <title>Introduction to Algorithms</title>
        <author>Thomas H. Cormen</author>
        <year>2022</year>
        <price currency="INR">1250.00</price>
    </book>
</library>
"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(sample_xml_content)


def parse_and_display_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return
    except ET.ParseError as err:
        print(f"Error: Invalid XML syntax - {err}")
        return

    lib_name = root.attrib.get("name", "Unknown Library")
    lib_city = root.attrib.get("city", "Unknown City")
    print(f"\n=== {lib_name} ({lib_city}) [Root Tag: <{root.tag}>] ===")
    print("-" * 86)
    print(f"{'ID':<8} {'Category':<16} {'Title':<28} {'Author':<20} {'Price':<12}")
    print("-" * 86)

    for book in root.findall("book"):
        book_id = book.get("id", "N/A")
        category = book.get("category", "General")
        title = book.findtext("title", default="Untitled").strip()
        author = book.findtext("author", default="Unknown").strip()
        price_elem = book.find("price")
        if price_elem is not None and price_elem.text:
            currency = price_elem.get("currency", "INR")
            price_display = f"{currency} {float(price_elem.text):.2f}"
        else:
            price_display = "N/A"

        print(f"{book_id:<8} {category:<16} {title:<28} {author:<20} {price_display:<12}")

    print("-" * 86 + "\n")


def main():
    xml_file = "library_catalog.xml"

    if not os.path.exists(xml_file):
        create_sample_xml(xml_file)

    parse_and_display_xml(xml_file)


if __name__ == "__main__":
    main()
