CREATE MIGRATION m1ugfh7wanozdanod6jmq6gk3vkqf5opyxyz7umrhu6f2oicmzflxq
    ONTO initial
{
  CREATE TYPE default::User {
      CREATE PROPERTY created_at: std::datetime {
          SET default := (std::datetime_current());
          SET readonly := true;
      };
      CREATE REQUIRED PROPERTY password: std::str;
      CREATE PROPERTY updated_at: std::datetime {
          CREATE REWRITE
              UPDATE 
              USING (std::datetime_of_statement());
      };
      CREATE REQUIRED PROPERTY username: std::str;
  };
  CREATE TYPE default::Booking {
      CREATE REQUIRED LINK user: default::User;
      CREATE PROPERTY comment: std::str;
      CREATE PROPERTY end_time: std::datetime;
      CREATE PROPERTY start_time: std::datetime;
  };
};
