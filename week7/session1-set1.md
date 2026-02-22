# Problem Set Version 1
# Problem 1: NFT Name Extractor
# Space Complexity: O(n) : creates a new list ls to store the names
# Time Complexity: O(n) : for loop that visits every element
def extract_nft_names(nft_collection):
    ls=[]
    for i in nft_collection:
        ls.append(i['name'])
    return ls 

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Future City", "creator": "UrbanArt", "value": 3.8}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(extract_nft_names(nft_collection))
print(extract_nft_names(nft_collection_2))
print(extract_nft_names(nft_collection_3))


# Problem 3: Identify Popular Creators
# Space Complexity: O(n) : 2n^1, for two for-loop, 
# Time Complexity: O(n) : for dictionary(n element), and list (only Unique)
def identify_popular_creators(nft_collection):
    creator_counts = {}
    popular_creators = []
    
    for nft in nft_collection:
        creator = nft.get("creator")
        if creator:
            creator_counts[creator] = creator_counts.get(creator, 0) + 1
            
    for creator, count in creator_counts.items():
        if count > 1:
            popular_creators.append(creator)
            
    return popular_creators

nft_collection = [
    {"name": "Abstract Horizon", "creator": "ArtByAlex", "value": 5.4},
    {"name": "Pixel Dreams", "creator": "DreamyPixel", "value": 7.2},
    {"name": "Urban Jungle", "creator": "ArtByAlex", "value": 4.5}
]

nft_collection_2 = [
    {"name": "Crypto Kitty", "creator": "CryptoPets", "value": 10.5},
    {"name": "Galactic Voyage", "creator": "SpaceArt", "value": 6.7},
    {"name": "Future Galaxy", "creator": "SpaceArt", "value": 8.3}
]

nft_collection_3 = [
    {"name": "Golden Hour", "creator": "SunsetArtist", "value": 8.9}
]

print(identify_popular_creators(nft_collection))
print(identify_popular_creators(nft_collection_2))
print(identify_popular_creators(nft_collection_3))


# Problem 5: NFT Tag Search
# Space Complexity: O(n): for the list
# Time Complexity: O(n^2): for nested for-loop
def search_nft_by_tag(nft_collections, tag):
    results = []
    for collection in nft_collections:
        for nft in collection:
            if tag in nft.get("tags", []):
                results.append(nft["name"])
                
    return results

nft_collections = [
    [
        {"name": "Abstract Horizon", "tags": ["abstract", "modern"]},
        {"name": "Pixel Dreams", "tags": ["pixel", "retro"]}
    ],
    [
        {"name": "Urban Jungle", "tags": ["urban", "landscape"]},
        {"name": "City Lights", "tags": ["modern", "landscape"]}
    ]
]

nft_collections_2 = [
    [
        {"name": "Golden Hour", "tags": ["sunset", "landscape"]},
        {"name": "Sunset Serenade", "tags": ["sunset", "serene"]}
    ],
    [
        {"name": "Pixel Odyssey", "tags": ["pixel", "adventure"]}
    ]
]

nft_collections_3 = [
    [
        {"name": "The Last Piece", "tags": ["finale", "abstract"]}
    ],
    [
        {"name": "Ocean Waves", "tags": ["seascape", "calm"]},
        {"name": "Mountain Peak", "tags": ["landscape", "adventure"]}
    ]
]

print(search_nft_by_tag(nft_collections, "landscape"))
print(search_nft_by_tag(nft_collections_2, "sunset"))
print(search_nft_by_tag(nft_collections_3, "modern"))


# Problem 7: Validate NFT Addition
# Space Complexity: O(1) : storing one variable only
# Time Complexity: O(n) : for-loop for going through the list

def validate_nft_actions(actions):
    balance = 0
    
    for a in actions:
        if a == "add":
            balance += 1
        elif a == "remove":
            balance -= 1
            
        if balance < 0:
            return False
            
    return balance == 0


actions = ["add", "add", "remove", "remove"]
actions_2 = ["add", "remove", "add", "remove"]
actions_3 = ["add", "remove", "remove", "add"]

print(validate_nft_actions(actions))
print(validate_nft_actions(actions_2))
print(validate_nft_actions(actions_3))
