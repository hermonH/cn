import java.net.InetAddress;
import java.net.UnknownHostException;
public class Local {
    public static void main(String[] args) {
        try {
            System.out.println(InetAddress.getLocalHost());
            System.out.println(InetAddress.getByName("flipkart.com"));
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }  
}