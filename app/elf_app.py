from src.elf_thread import *



def main(args=None):
    
    # Start all threads
    elf_gui_thread.start()
    elf_trjstd_thread.start()

    # Wait all threads to stop
    elf_gui_thread.join()
    elf_trjstd_thread.join()



if __name__ == '__main__':
    main()