

def chunk_text(text: str):
    chunks=[]
    for x in range(0,len(text),5):
        chunks.append(text[x:x+5])
    return chunks
    
    