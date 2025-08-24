"""mealie auto tagger - Automatically apply a mealie lable to items added to your shopping list

This module starts the web server and runs mealie auto tagger.
"""

import uvicorn

def main():
    uvicorn.run(
        "mealie_auto_tagger.app:app",
        host="0.0.0.0",
        port=8081,
    )
if __name__ == "__main__":
    main()
