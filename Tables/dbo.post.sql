CREATE TABLE [dbo].[post]
(
[id] [int] NOT NULL IDENTITY(1, 1),
[title] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[text] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[publish_date] [datetime] NULL,
[user_id] [int] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[post] ADD CONSTRAINT [PK__post__3213E83FDDD06797] PRIMARY KEY CLUSTERED  ([id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[post] ADD CONSTRAINT [FK__post__user_id__267ABA7A] FOREIGN KEY ([user_id]) REFERENCES [dbo].[user] ([id])
GO
