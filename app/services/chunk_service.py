

def chunk_text(text: str):
    chunks=[]
    for x in range(0,len(text),500):
        chunks.append(text[x:x+500])
    return chunks
    
    