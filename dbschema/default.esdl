module default {
  type User {
    required username: str;
    required password: str;
    created_at: datetime{
        default := (datetime_current());
        readonly := true;
        };
    updated_at: datetime {
          rewrite update using (datetime_of_statement());
        };
  }
  type Booking{
    required user: User;
    start_time: datetime;
    end_time: datetime;
    comment: str;
  }

}