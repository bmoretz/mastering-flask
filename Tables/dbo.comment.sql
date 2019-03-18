CREATE TABLE [dbo].[comment]
(
[id] [int] NOT NULL IDENTITY(1, 1),
[name] [varchar] (255) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[text] [varchar] (max) COLLATE SQL_Latin1_General_CP1_CI_AS NULL,
[date] [datetime] NULL,
[post_id] [int] NULL
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[comment] ADD CONSTRAINT [PK__comment__3213E83F6DF2556B] PRIMARY KEY CLUSTERED  ([id]) ON [PRIMARY]
GO
ALTER TABLE [dbo].[comment] ADD CONSTRAINT [FK__comment__post_id__29572725] FOREIGN KEY ([post_id]) REFERENCES [dbo].[post] ([id])
GO
