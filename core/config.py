class Settings:
    PROJECT_NAME: str = "Moj app"
    PROJECT_VERSION: str = "1.0.0"
    # PROJECT_DESCRIPTION: str = """
    #     ChimichangApp API helps you do awesome stuff. 🚀
    #
    #     ## Items
    #
    #     You can **read items**.
    #
    #     ## Users
    #
    #     You will be able to:
    #
    #     * **Create users** (_not implemented_).
    #     * **Read users** (_not implemented_).
    #     """
    TERMS_OF_SERVICE = "http://example.com/terms/",
    CONTACT = {
                  "name": "Deadpoolio the Amazing",
                  "url": "http://x-force.example.com/contact/",
                  "email": "dp@x-force.example.com",
              },
    LICENCE_INFO = {
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    }


settings = Settings()
