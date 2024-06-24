TOOLS=[
    {
      "type": "function",
      "function": {
        "name": "check_bike_availability",
        "description": "Checking available bikes for specified dates",
        "parameters": {
          "type": "object",
          "properties": {
            "start_date": {
              "type": "string",
              "description": "Bike rental start date"
            },
            "end_date": {
              "type": "string",
              "description": "Bike rental end date"
            },
            "cc": {
              "type": "number",
              "description": "Power of bike"
            }
          },
          "required": ["start_date", "end_date", "cc"]
        }
      }
    },
     {
      "type": "function",
      "function": {
        "name": "get_current_datetime",
        "description": "get current time",
        "parameters": {
          "type": "object",
          "properties": {
            "date_time": {
              "type": "string",
              "description": "get current Date&Time"
            }
          },
        }
      }
    },
    {
      "type": "function",
      "function": {
        "name": "create_booking",
        "description": "Create a booking for a bike",
        "parameters": {
            "type": "object",
            "properties": {
                "number": {
                    "type": "integer",
                    "description": "Bike number"
                },
                "cc": {
                    "type": "integer",
                    "description": "Power of bike"
                },
                "name": {
                    "type": "string",
                    "description": "Name of the person booking the bike"
                },
                "contact": {
                    "type": "string",
                    "description": "Contact information of the person booking the bike"
                },
                "start_date": {
                    "type": "string",
                    "description": "Bike rental start date"
                },
                "end_date": {
                    "type": "string",
                    "description": "Bike rental end date"
                }
            },
            "required": ["number", "cc", "name", "contact", "start_date", "end_date"]
        }
    }
    }
  ]