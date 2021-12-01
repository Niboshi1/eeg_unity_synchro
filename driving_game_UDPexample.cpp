using UnityEngine;
using System.Net.Sockets;
using System.Text;
 
public class UDPClient : MonoBehaviour
{
    // broadcast address
    public string host = "127.0.0.1";
    public int port = 8000;
    private UdpClient client;
 
    void Start ()
    {
        client = new UdpClient();
        client.Connect(host, port);
 
        byte[] dgram = Encoding.UTF8.GetBytes("hello!");
        client.Send(dgram, dgram.Length);
    }
 
    void Update ()
    {
    }
 
    void OnApplicationQuit()
    {
        client.Close();
    }
}