import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;
import java.net.UnknownHostException;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
public class Server {

    public static void main(String[] args) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");  
        LocalDateTime now = LocalDateTime.now(); 
        try{
            ServerSocket ss = new ServerSocket(6666);
            Socket s = ss.accept();

            DataInputStream din = new DataInputStream(s.getInputStream());
            String str = (String) din.readUTF();
            System.out.println(str);

            DataOutputStream dos = new DataOutputStream(s.getOutputStream());
            dos.writeUTF(dtf.format(now));
            dos.flush();

            dos.close();
            din.close();
            s.close();
            ss.close();
        }catch(UnknownHostException ue){
            ue.printStackTrace();
        }catch(IOException ie){
            ie.printStackTrace();
        }
    }    
}
