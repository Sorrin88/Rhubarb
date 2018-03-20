import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.io.PrintStream;
import java.io.Reader;
import java.net.Socket;

public class CheckConnect {
    private static final String URL = "netsrv.cim.rhul.ac.uk";
    private static final int PORT = 1812;

    public static void main(String[] arrstring) {
        if (arrstring.length < 2) {
            System.err.println("Usage: java CheckConnect username password");
            System.exit(-1);
        }
        String string = arrstring[0];
        String string2 = arrstring[1];
        try {
            Socket socket = new Socket("netsrv.cim.rhul.ac.uk", 1812);
            Throwable throwable = null;
            try {
                PrintStream printStream = new PrintStream(socket.getOutputStream());
                Throwable throwable2 = null;
                try {
                    BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                    Throwable throwable3 = null;
                    try {
                        System.out.format("Trying to connect to %s:%d as %s\n", "netsrv.cim.rhul.ac.uk", 1812, string);
                        printStream.println(string);
                        printStream.println(string2);
                        printStream.flush();
                        String string3 = bufferedReader.readLine();
                        if (string3.contains("success")) {
                            System.out.println("Successfully logged in as " + string);
                        } else {
                            System.out.println("Got unexpected response " + string3);
                        }
                    }
                    catch (Throwable throwable4) {
                        throwable3 = throwable4;
                        throw throwable4;
                    }
                    finally {
                        if (bufferedReader != null) {
                            if (throwable3 != null) {
                                try {
                                    bufferedReader.close();
                                }
                                catch (Throwable throwable5) {
                                    throwable3.addSuppressed(throwable5);
                                }
                            } else {
                                bufferedReader.close();
                            }
                        }
                    }
                }
                catch (Throwable throwable6) {
                    throwable2 = throwable6;
                    throw throwable6;
                }
                finally {
                    if (printStream != null) {
                        if (throwable2 != null) {
                            try {
                                printStream.close();
                            }
                            catch (Throwable throwable7) {
                                throwable2.addSuppressed(throwable7);
                            }
                        } else {
                            printStream.close();
                        }
                    }
                }
            }
            catch (Throwable throwable8) {
                throwable = throwable8;
                throw throwable8;
            }
            finally {
                if (socket != null) {
                    if (throwable != null) {
                        try {
                            socket.close();
                        }
                        catch (Throwable throwable9) {
                            throwable.addSuppressed(throwable9);
                        }
                    } else {
                        socket.close();
                    }
                }
            }
        }
        catch (Exception exception) {
            System.err.println("Error establishing connection: " + exception);
            System.exit(-1);
        }
        try {
            Thread.sleep(1000);
        }
        catch (Exception exception) {
            // empty catch block
        }
    }
}
