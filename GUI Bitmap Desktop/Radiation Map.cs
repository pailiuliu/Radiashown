using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using IronPython.Hosting;
using System.IO;
using System.Runtime.InteropServices;

namespace GUI_Bitmap_Desktop
{
    public partial class Radiashown : Form
    {
        Bitmap image1, image2;
        public Radiashown()
        {
            InitializeComponent();
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
            //bitmap
            image1 = new Bitmap(@"C:\Users\Marilyn\Desktop\Engineering 5\4TB6\itb137.bmp", true);

            //load bmp in picturebox1
            pictureBox1.Image = image1;
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            //AllocConsole();
        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {
            textBox1.Text = "test";
            // 1) Create engine
            var engine = Python.CreateEngine();

            // 2) Provide script and arguments
            var script = @"C:\Users\Marilyn\Desktop\Engineering 5\4TB6\testStream.py";
            var source = engine.CreateScriptSourceFromFile(script);

            // 3) Output redirect
            var eIO = engine.Runtime.IO;

            var results = new MemoryStream();
            eIO.SetOutput(results, Encoding.Default);

            // 4) Execute script
            var scope = engine.CreateScope();
            source.Execute(scope);

            // 5) Display output
            string str(byte[] x) => Encoding.Default.GetString(x);

            Console.WriteLine();
            Console.WriteLine("Results:");
            Console.WriteLine(str(results.ToArray()));


            // Display the pixel format in Label1.
            textBox1.Text = str(results.ToArray());
        }
          

        private void startButton_Click(object sender, EventArgs e)
        {
            startButton.BackColor = Color.FromName("Green");
            startButton.Text = "Sweeping";
            startButton.Enabled = false;

            emergencyButton.Visible = true;
            setupButton.Visible = false;
        }

        private void emergencyButton_Click(object sender, EventArgs e)
        {
            startButton.BackColor = Color.FromName("FireBrick");
            startButton.Text = "Returning Home";
            startButton.Enabled = true;

            emergencyButton.Visible = false;
        }

        //This is a placeholder
        private void home_Click(object sender, EventArgs e)
        {
            startButton.BackColor = Color.FromName("Buttonshadow");
            startButton.Text = "Start Sweep";
            startButton.Enabled = true;

            emergencyButton.Visible = false;
            setupButton.Visible = true;
        }

        private void setupButton_Click(object sender, EventArgs e)
        {
            //this.Hide();
            radSetup fsetup = new radSetup();
            fsetup.ShowDialog();
            //this.Close();
        }


        /*[DllImport("kernel32.dll", SetLastError = true)]
        [return: MarshalAs(UnmanagedType.Bool)]
        static extern bool AllocConsole();
        */

    }
}
