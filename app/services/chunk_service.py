import re

#def chunk_text(text: str,chunk_size: int = 500, overlap: int = 0):
    #chunks=[]
    #for x in range(0,len(text),chunk_size):
        #chunks.append(text[x+overlap:x+chunk_size])
    #return chunks
    
def chunk_text(text: str,chunk_size: int = 500, overlap: int = 0):
    chunks=[]
    start =0
    if overlap >= chunk_size or overlap < 0:
        raise ValueError("Overlap must be smaller than chunk size and greater than or equal to 0")
    if chunk_size <=0:
        raise ValueError("Chunk size should be greater than 0")
    while start < len(text):
        chunks.append(text[start : start+chunk_size ])
        start = start + chunk_size - overlap
    return chunks

def sentence_chunk_text(text: str, chunk_size: int=500):
    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = []
    for sentence in sentences:
        candidate = " ".join(current_chunk + [sentence])
        if len(candidate) <= chunk_size:
            current_chunk.append(sentence)
        else:
            if current_chunk:
                chunks.append(" ".join(current_chunk))
            current_chunk = sentence
    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks
