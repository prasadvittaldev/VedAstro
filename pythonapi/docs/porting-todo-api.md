# API porting to-do

The C# API project contains the following classes. Each class needs an equivalent module in the Python `vedastro_api` package. Use this list to track porting progress.

| .NET class (path) | Purpose | Target Python module | Status |
| --- | --- | --- | --- |
| `Program.cs` | Azure Functions entry point | n/a (FastAPI uses `vedastro_api.__init__`) | n/a |
| `ApiLogger.cs` | centralised logging for API calls | `vedastro_api/api_logger.py` | DONE |
| `ThrottleManager.cs` | throttling and rate limiting helpers | `vedastro_api/throttle_manager.py` | DONE |
| `FrontDesk/BirthTimeFinderAPI.cs` | endpoints for birth-time estimation workflows | `vedastro_api/birth_time_finder.py` | TODO |
| `FrontDesk/EventsChartAPI.cs` | generate and email event charts | `vedastro_api/events_chart.py` | TODO |
| `FrontDesk/GeneralAPI.cs` | miscellaneous endpoints (favicon, home, hash) | `vedastro_api/general.py` | DONE |
| `FrontDesk/MatchAPI.cs` | relationship compatibility calculations | `vedastro_api/match.py` | TODO |
| `FrontDesk/MessageAPI.cs` | messaging and notifications | `vedastro_api/message.py` | TODO |
| `FrontDesk/PersonAPI.cs` | CRUD for person profiles | `vedastro_api/person.py` | TODO |
| `FrontDesk/SignInAPI.cs` | OAuth sign-in endpoints | `vedastro_api/sign_in.py` | TODO |
| `FrontDesk/SkyChartAPI.cs` | sky chart image generation | `vedastro_api/sky_chart.py` | TODO |
| `FrontDesk/SubscriptionAPI.cs` | subscribe/unsubscribe for updates | `vedastro_api/subscription.py` | TODO |
| `FrontDesk/OpenAPI.cs` | open API utilities and call listings | `vedastro_api/open_api.py` | TODO |
| `FrontDesk/WebsiteLoggerAPI.cs` | website error/debug logging | `vedastro_api/website_logger.py` | TODO |
| `TableData/CallStatusEntity.cs` | table storage entity for call status | `vedastro_api/tabledata/call_status.py` | DONE |
| `TableData/OpenAPILogBookEntity.cs` | table storage entity for API log book | `vedastro_api/tabledata/openapi_log_book.py` | DONE |
| `TableData/OpenAPIErrorBookEntity.cs` | table storage entity for API error log | `vedastro_api/tabledata/openapi_error_book.py` | DONE |
| `TableData/AnalyticsEntity.cs` | table storage entity for analytics | `vedastro_api/tabledata/analytics.py` | DONE |
| `TableData/GeoLocationCacheEntity.cs` | table storage entity for geolocation cache | `vedastro_api/tabledata/geolocation_cache.py` | DONE |

Tick off each item as you port the corresponding class and its functions to Python.
