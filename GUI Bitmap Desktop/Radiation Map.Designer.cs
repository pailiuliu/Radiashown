namespace GUI_Bitmap_Desktop
{
    partial class Radiashown
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.textBox1 = new System.Windows.Forms.TextBox();
            this.startButton = new System.Windows.Forms.Button();
            this.setupButton = new System.Windows.Forms.Button();
            this.emergencyButton = new System.Windows.Forms.Button();
            this.homeCheckBox = new System.Windows.Forms.CheckBox();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Location = new System.Drawing.Point(18, 18);
            this.pictureBox1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(1284, 815);
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            this.pictureBox1.Click += new System.EventHandler(this.pictureBox1_Click);
            // 
            // textBox1
            // 
            this.textBox1.AcceptsReturn = true;
            this.textBox1.AllowDrop = true;
            this.textBox1.Location = new System.Drawing.Point(1354, 807);
            this.textBox1.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.textBox1.MaximumSize = new System.Drawing.Size(3000, 2000);
            this.textBox1.Name = "textBox1";
            this.textBox1.Size = new System.Drawing.Size(271, 26);
            this.textBox1.TabIndex = 1;
            this.textBox1.TextChanged += new System.EventHandler(this.textBox1_TextChanged);
            // 
            // startButton
            // 
            this.startButton.BackColor = System.Drawing.SystemColors.ButtonShadow;
            this.startButton.FlatAppearance.BorderColor = System.Drawing.Color.Black;
            this.startButton.FlatAppearance.MouseDownBackColor = System.Drawing.Color.Green;
            this.startButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.startButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.startButton.ForeColor = System.Drawing.SystemColors.ControlText;
            this.startButton.Location = new System.Drawing.Point(1353, 53);
            this.startButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.startButton.Name = "startButton";
            this.startButton.Size = new System.Drawing.Size(262, 78);
            this.startButton.TabIndex = 4;
            this.startButton.Text = "Start Sweep";
            this.startButton.UseVisualStyleBackColor = false;
            this.startButton.Click += new System.EventHandler(this.startButton_Click);
            // 
            // setupButton
            // 
            this.setupButton.AccessibleName = "setupButton";
            this.setupButton.BackColor = System.Drawing.SystemColors.ButtonShadow;
            this.setupButton.FlatAppearance.BorderColor = System.Drawing.Color.DimGray;
            this.setupButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.setupButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.setupButton.Location = new System.Drawing.Point(1354, 150);
            this.setupButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.setupButton.Name = "setupButton";
            this.setupButton.Size = new System.Drawing.Size(262, 78);
            this.setupButton.TabIndex = 5;
            this.setupButton.Text = "Setup";
            this.setupButton.UseVisualStyleBackColor = false;
            this.setupButton.Click += new System.EventHandler(this.setupButton_Click);
            // 
            // emergencyButton
            // 
            this.emergencyButton.AccessibleName = "";
            this.emergencyButton.BackColor = System.Drawing.Color.Firebrick;
            this.emergencyButton.FlatAppearance.BorderColor = System.Drawing.Color.DimGray;
            this.emergencyButton.FlatStyle = System.Windows.Forms.FlatStyle.Popup;
            this.emergencyButton.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.emergencyButton.Location = new System.Drawing.Point(1353, 150);
            this.emergencyButton.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.emergencyButton.Name = "emergencyButton";
            this.emergencyButton.Size = new System.Drawing.Size(262, 78);
            this.emergencyButton.TabIndex = 6;
            this.emergencyButton.Text = "Emergency Stop";
            this.emergencyButton.UseVisualStyleBackColor = false;
            this.emergencyButton.Visible = false;
            this.emergencyButton.Click += new System.EventHandler(this.emergencyButton_Click);
            // 
            // homeCheckBox
            // 
            this.homeCheckBox.AutoSize = true;
            this.homeCheckBox.Location = new System.Drawing.Point(1404, 845);
            this.homeCheckBox.Name = "homeCheckBox";
            this.homeCheckBox.Size = new System.Drawing.Size(163, 24);
            this.homeCheckBox.TabIndex = 7;
            this.homeCheckBox.Text = "Robots Are Home";
            this.homeCheckBox.UseVisualStyleBackColor = true;
            this.homeCheckBox.Click += new System.EventHandler(this.home_Click);
            // 
            // Radiashown
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.AppWorkspace;
            this.ClientSize = new System.Drawing.Size(1676, 892);
            this.Controls.Add(this.textBox1);
            this.Controls.Add(this.homeCheckBox);
            this.Controls.Add(this.emergencyButton);
            this.Controls.Add(this.setupButton);
            this.Controls.Add(this.startButton);
            this.Controls.Add(this.pictureBox1);
            this.Margin = new System.Windows.Forms.Padding(4, 5, 4, 5);
            this.Name = "Radiashown";
            this.Text = "Radiashown";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox1;
        private System.Windows.Forms.TextBox textBox1;
        private System.Windows.Forms.Button startButton;
        private System.Windows.Forms.Button setupButton;
        private System.Windows.Forms.Button emergencyButton;
        private System.Windows.Forms.CheckBox homeCheckBox;
    }
}

