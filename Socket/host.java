import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.io.PrintStream;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.logging.Level;
import java.util.logging.Logger;
import java.io.ByteArrayOutputStream;


public class host {

    public static void main(String srgs[]) {

        int count = 0;

        //hard code to use port 8080
        try (ServerSocket serverSocket = new ServerSocket(8080)) {
            
            System.out.println("I'm waiting here: " + serverSocket.getLocalPort());
            
            while (true) {
                
                try {
                    Socket socket = serverSocket.accept();
                            
                    count++;
                    System.out.println("#" + count + " from "
                            + socket.getInetAddress() + ":" 
                            + socket.getPort());
                    
                    /*  move to background thread
                    OutputStream outputStream = socket.getOutputStream();
                    try (PrintStream printStream = new PrintStream(outputStream)) {
                        printStream.print("Hello from Raspberry Pi, you are #" + count);
                    }
                    */
                    HostThread myHostThread = new HostThread(socket, count);
                    myHostThread.start();
                    
                } catch (IOException ex) {
                    System.out.println(ex.toString());
                }
            }
        } catch (IOException ex) {
            System.out.println(ex.toString());
        }
    }
    
    private static class HostThread extends Thread{
        
        private Socket hostThreadSocket;
        int cnt;
        
        HostThread(Socket socket, int c){
            hostThreadSocket = socket;
            cnt = c;
        }

        @Override
        public void run() {

            OutputStream outputStream;
            InputStream inputStream;
            try {
               
                inputStream = hostThreadSocket.getInputStream();
               
                 ByteArrayOutputStream byteArrayOutputStream =
                        new ByteArrayOutputStream(1024);
                byte[] buffer = new byte[1024];

                int bytesRead;
                while ((bytesRead = inputStream.read(buffer)) != -1){
                    byteArrayOutputStream.write(buffer, 0, bytesRead);
                }
                String response = byteArrayOutputStream.toString("UTF-8");
                System.out.println(response);
            } catch (IOException ex) {
                Logger.getLogger(host.class.getName()).log(Level.SEVERE, null, ex);
            }
            finally{
                try {
                    hostThreadSocket.close();
                } catch (IOException ex) {
                    Logger.getLogger(host.class.getName()).log(Level.SEVERE, null, ex);
                }
            }
        }
    }
}
