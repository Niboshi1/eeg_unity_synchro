from camera_input import capture_camera
from camera_UDP import udp_with_game
from settings import OPTIONS
from multiprocessing import Process

#udp_with_game(HOST="127.0.0.1", PORT=8000)
#capture_camera(OPTIONS)
 
def main():
    p1 = Process(target=udp_with_game, args=("127.0.0.1", 8000,))
    p1.start()

    p2 = Process(target=capture_camera, args=(OPTIONS, ))
    p2.start()

    p1.join()
    p2.join()

if __name__ == '__main__':
    main()