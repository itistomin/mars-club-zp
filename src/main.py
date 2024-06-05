from calendar import Calendar
from datetime import datetime
from dateutil.relativedelta import relativedelta

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

month_name_mapping = {
    1: "Січень",
    2: "Лютий",
    3: "Березень",
    4: "Квітень",
    5: "Травень",
    6: "Червень",
    7: "Липень",
    8: "Серпень",
    9: "Вересень",
    10: "Жовтень",
    11: "Листопад",
    12: "Грудень",
}


@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/booking")
def book_table(
        request: Request,
        year: int = datetime.today().year,
        month: int = datetime.today().month,
):
    dates_range = Calendar().monthdayscalendar(year, month)
    selected_date = datetime(year, month, 1)
    navigation_dates = {
        "prev": selected_date - relativedelta(months=1),
        "next": selected_date + relativedelta(months=1),
    }

    return templates.TemplateResponse(
        "booking/booking.html",
        {
            "request": request,
            "dates_range": dates_range,
            "navigation_dates": navigation_dates,
            "selected_date": selected_date,
            "month_name": month_name_mapping[month],
        }
    )


@app.get("/auth")
def read_root(request: Request):
    return templates.TemplateResponse("auth/auth.html", {"request": request})
