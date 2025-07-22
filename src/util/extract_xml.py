def extract_xml_tag(content: str, tag: str) -> str:
    start_tag = f"<{tag}>"
    end_tag = f"</{tag}>"
    start_index = content.find(start_tag)
    if start_index == -1:
        return None
    end_index = content.find(end_tag, start_index + len(start_tag))
    if end_index == -1:
        return None

    return content[start_index + len(start_tag) : end_index].strip()
