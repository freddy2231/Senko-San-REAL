# Simple Logger
import sys
import traceback
from datetime import datetime

class Logger:
    __do_not_save = False
    __filename = "log.log"
    __errs = "errors.log"

    def getLastLine(self):
        try:
            if not self.__do_not_save:
                line = 0
                handle = open(self.__errs, "r+")
                tmp = ""
                for l in handle:
                    tmp = l
                    line = line + 1
                handle.close()
                if not tmp == '\n':
                    line = line - 1
                return line
            else:
                return None
        except:
            # Don't replace this block with self.logErr function this could cause spam when getting file access error
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
            try:
                if self.__do_not_save == False:
                    f = open(self.__filename,"a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\n")
                    f.close()
                    f = open(self.__errs, "a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\n")
                    f.close()
            except IOError:
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] File named '" + str(self.__filename) + "' is missing or you have no permmission to write\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Turning off writing to log file\033[m\n")
                self.__do_not_save = True

    def err(self, caller, msg):
        try:
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\033[m\n")
        
            if self.__do_not_save == False:
                f = open(self.__filename,"a+")
                f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                f.close()
                f = open(self.__errs, "a+")
                f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                f.close()
        except:
            # Don't replace this block with self.logErr function this could cause spam when getting file access error
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
            try:
                if self.__do_not_save == False:
                    f = open(self.__filename,"a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
                    f = open(self.__errs, "a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
            except IOError:
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] File named '" + str(self.__filename) + "' is missing or you have no permmission to write\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Turning off writing to log file\033[m\n")
                self.__do_not_save = True
            except:
                sys.stdout.write("\033[33m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Unexpected error\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
        return

    def warn(self, caller, msg):
        try:
            sys.stdout.write("\033[33m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/WARN] " + str(msg) + "\033[m\n")
        
            if self.__do_not_save == False:
                f = open(self.__filename,"a+")
                f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/WARN] " + str(msg) + "\n")
                f.close()
        except:
            # Don't replace this block with self.logErr function this could cause spam when getting file access error
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
            try:
                if self.__do_not_save == False:
                    f = open(self.__filename,"a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
                    f = open(self.__errs, "a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
            except IOError:
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] File named '" + str(self.__filename) + "' is missing or you have no permmission to write\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Turning off writing to log file\033[m\n")
                self.__do_not_save = True
            except:
                sys.stdout.write("\033[33m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Unexpected error\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
        return

    def info(self, caller, msg):
        try:
            sys.stdout.write("\033[m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/INFO] " + str(msg) + "\033[m\n")
        
            if self.__do_not_save == False:
                f = open(self.__filename,"a+")
                f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/INFO] " + str(msg) + "\n")
                f.close()
        except:
            # Don't replace this block with self.logErr function this could cause spam when getting file access error
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
            try:
                if self.__do_not_save == False:
                    f = open(self.__filename,"a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
                    f = open(self.__errs, "a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
            except IOError:
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] File named '" + str(self.__filename) + "' is missing or you have no permmission to write\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Turning off writing to log file\033[m\n")
                self.__do_not_save = True
            except:
                sys.stdout.write("\033[33m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Unexpected error\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
        return

    def debug(self, caller, msg):
        try:
            sys.stdout.write("\033[36m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/DEBUG] " + str(msg) + "\033[m\n")
        
            if self.__do_not_save == False:
                f = open(self.__filename,"a+")
                f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/DEBUG] " + str(msg) + "\n")
                f.close()
        except:
            # Don't replace this block with self.logErr function this could cause spam when getting file access error
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
            sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
            try:
                if self.__do_not_save == False:
                    f = open(self.__filename,"a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
                    f = open(self.__errs, "a+")
                    f.write("[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [" + str(caller) + "/ERROR] " + str(msg) + "\n")
                    f.close()
            except IOError:
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] File named '" + str(self.__filename) + "' is missing or you have no permmission to write\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Turning off writing to log file\033[m\n")
                self.__do_not_save = True
            except:
                sys.stdout.write("\033[33m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] Unexpected error\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] SimpleLogger error traceback (NOT A LOGGER CRASH)\033[m\n")
                sys.stdout.write("\033[31m[" + datetime.now().strftime('%d-%m-%Y %H:%M:%S') + "] [SimpleLogger/ERROR] " + traceback.format_exc() + "\033[m\n")
        return