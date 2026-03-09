def airline_delay_statistics(df):

    airline_stats = df.groupby("airline").agg({

        "arrival_delay_minutes": ["mean","max","min"],
        "departure_delay_minutes": ["mean","max","min"],
        "total_delay": ["mean"]

    })

    return airline_stats