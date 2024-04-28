import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.Socket;
import java.net.UnknownHostException;
import java.time.format.DateTimeFormatter;  
import java.time.LocalDateTime;   
public class Client {

    public static void main(String[] args) {
        DateTimeFormatter dtf = DateTimeFormatter.ofPattern("yyyy/MM/dd HH:mm:ss");  
        LocalDateTime now = LocalDateTime.now(); 
        try{
            Socket n = new Socket("localHost",6666);

            DataOutputStream dos = new DataOutputStream(n.getOutputStream());
            dos.writeUTF(dtf.format(now));
            dos.flush();

            DataInputStream din = new DataInputStream(n.getInputStream());
            String str = (String) din.readUTF();
            System.out.println(str);

            dos.close();
            din.close();
            n.close();
        }catch(UnknownHostException ue){
            ue.printStackTrace();
        }catch(IOException ie){
            ie.printStackTrace();
        }
    }  
}
