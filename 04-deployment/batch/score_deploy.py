from prefect.deployments import Deployment
from prefect.orion.schemas.schedules import CronSchedule
from score import ride_duration_prediction

deployment = Deployment.build_from_flow(
    flow=ride_duration_prediction,
    name="ride_duration_prediction",
    parameters={
        "taxi_type": "green",
        "run_id": "125e1f20f7a544738d959329a37c9ecb",
    },
    schedule=CronSchedule(cron="0 3 2 * *"),
    work_queue_name="ml",
)

deployment.apply()
