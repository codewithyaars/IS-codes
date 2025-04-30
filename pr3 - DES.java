import java.security.InvalidKeyException;
import java.security.NoSuchAlgorithmException;
import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;

public class DES {
    public static void main(String[] args) {
        try {
            System.out.println("************Message Encryption Using DES Algorithm************");
            
            // Generating a DES key
            KeyGenerator keygenerator = KeyGenerator.getInstance("DES");
            SecretKey myDesKey = keygenerator.generateKey();

            // Creating the cipher object
            Cipher desCipher;
            desCipher = Cipher.getInstance("DES/ECB/PKCS5Padding");

            // Initializing the cipher for encryption
            desCipher.init(Cipher.ENCRYPT_MODE, myDesKey);
            
            String text = "Secret Information";
            byte[] textBytes = text.getBytes();
            
            System.out.println("Message [Byte Format]: " + textBytes);
            System.out.println("Message: " + new String(textBytes));

            // Encrypting the text
            byte[] textEncrypted = desCipher.doFinal(textBytes);
            System.out.println("Encrypted Message: " + new String(textEncrypted));

            // Initializing the cipher for decryption
            desCipher.init(Cipher.DECRYPT_MODE, myDesKey);

            // Decrypting the text
            byte[] textDecrypted = desCipher.doFinal(textEncrypted);
            System.out.println("Decrypted Message: " + new String(textDecrypted));

        } catch (NoSuchAlgorithmException e) {
            e.printStackTrace();
        } catch (NoSuchPaddingException e) {
            e.printStackTrace();
        } catch (InvalidKeyException e) {
            e.printStackTrace();
        } catch (IllegalBlockSizeException e) {
            e.printStackTrace();
        } catch (BadPaddingException e) {
            e.printStackTrace();
        }
    }
}
