# JAVA DATABASE

### Coneector Class

```
import java.sql.Connection;
import java.sql.DriverManager;

public class ConnectionClass {

    public Connection connect() {
        String url = "jdbc:mysql://localhost:3306/cse20";
        String username = "root";
        String password = "";
        Connection connection = null;

        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            connection = DriverManager.getConnection(url, username, password);
            System.out.println("Connected to the database successfully!");

        } catch (Exception e) {
            System.out.println(e);
        }

        return connection;
    }

}
```


### Select Query
```
        ConnectionClass conn = new ConnectionClass();
        connection = conn.connect();

        String q = "select * from student";

        try {
            pst = connection.prepareStatement(q);
            res = pst.executeQuery();

            jTextArea1.setText("");

            while (res.next()) {

                int id = res.getInt("id");
                String name = res.getString("reg");
                String email = res.getString("name");

                jTextArea1.append(id + "\t" + name + "\t" + email + "\n");
            }

            connection.close();
            res.close();
        } catch (Exception e) {
            System.out.println(e);
        }
```

### Insert Query
```
        ConnectionClass conn = new ConnectionClass();
        connection = conn.connect();

        String q = "insert into student (id, reg, name) values (?,?,?)";

        try {
            pst = connection.prepareStatement(q);

            pst.setString(1, idFiled.getText());
            pst.setString(2, regField.getText());
            pst.setString(3, nameField.getText());

            pst.execute();
            connection.close();
        } catch (Exception e) {
            System.out.println(e);
        }
```

### Update Query
```
        ConnectionClass conn = new ConnectionClass();
        connection = conn.connect();

        String q = "UPDATE student SET reg = ?, name = ? WHERE id = ?";

        try {
            pst = connection.prepareStatement(q);
            pst.setString(1, regupdate.getText());
            pst.setString(2, nameupdate.getText());
            pst.setString(3, idupdate.getText());
            pst.execute();
            connection.close();
        } catch (Exception e) {
            System.out.println(e);
        }
```

### Delete Query
```
        ConnectionClass conn = new ConnectionClass();
        connection = conn.connect();

        String q = "DELETE FROM student WHERE id = ?";

        try {
            pst = connection.prepareStatement(q);
            pst.setString(1, deleteField.getText());
            pst.execute();
            connection.close();
        } catch (Exception e) {
            System.out.println(e);
        }
```

### Search Query
```
        ConnectionClass conn = new ConnectionClass();
        Connection connection = conn.connect();
        
        String q = "SELECT * FROM student WHERE name LIKE ?";
        
        try {
            PreparedStatement pst = connection.prepareStatement(q);
            pst.setString(1, "%" + searchField.getText() + "%"); 
            ResultSet res = pst.executeQuery();
        
            jTextArea1.setText("");
        
            while (res.next()) {
                int id = res.getInt("id");
                String reg = res.getString("reg");
                String name = res.getString("name");
        
                jTextArea1.append(id + "\t" + reg + "\t" + name + "\n");
            }
            
            res.close(); 
            pst.close(); 
            connection.close(); 
        
        } catch (Exception e) {
            e.printStackTrace(); 
        }
```

### Select Query with ID
```
        ConnectionClass conn = new ConnectionClass();
        connection = conn.connect();

        String q = "select * from student  where id = ?";

        try {
            pst = connection.prepareStatement(q);
            pst.setInt(1, Integer.parseInt( jTextField1.getText()));
            res = pst.executeQuery();
            jTextArea1.setText("");
            
            while (res.next()) {
                int id = res.getInt("id");
                String name = res.getString("reg");
                String email = res.getString("name");
                jTextArea1.append(id + "\t" + name + "\t" + email + "\n");
            }
            connection.close();
            res.close();
        } catch (Exception e) {
            System.out.println(e);
        }
```


### Thread 
```
    Runnable task1 = () -> {
        for (int i = 1; i <= 10; i++) {
            System.out.println("Thread-1 - Number: " + i);
            try {
                Thread.sleep(100); 
            } catch (InterruptedException e) {
                System.out.println("Thread-1 interrupted.");
            }
        }
    };

    Runnable task2 = () -> {
        for (int i = 11; i <= 20; i++) {
            System.out.println("Thread-2 - Number: " + i);
            try {
                Thread.sleep(100); 
            } catch (InterruptedException e) {
                System.out.println("Thread-2 interrupted.");
            }
        }
    };

    Thread thread1 = new Thread(task1);
    Thread thread2 = new Thread(task2);

    thread1.start();
    thread2.start();
```
