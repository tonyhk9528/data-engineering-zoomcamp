with green_tripdata as (
    select * from {{ source('raw_data', 'yellow_tripdata') }}
),

yellow_tripdata as (
    select * from {{ source('raw_data', 'yellow_tripdata') }}
),

trips_unioned as (
    select* from green_tripdata
    union all 
    select * from yellow_tripdata
)

select * from trips_unioned